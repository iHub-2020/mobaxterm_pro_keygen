#!/usr/bin/env python3
"""
Title: MobaXterm Pro KeyGen
Version: 1.0.2
Author: Reyanmatic
Date: 2025-12-01
Description: A web-based tool to generate MobaXterm Professional license keys.
             Backend logic handles encryption and ZIP file generation.
"""

import os
import sys
import zipfile
import io
from flask import Flask, request, send_file, make_response

app = Flask(__name__)

# --- 核心加解密和编码逻辑 ---
VariantBase64Table = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/='
VariantBase64Dict = {i: VariantBase64Table[i] for i in range(len(VariantBase64Table))}
VariantBase64ReverseDict = {VariantBase64Table[i]: i for i in range(len(VariantBase64Table))}

def VariantBase64Encode(bs: bytes):
    result = b''
    blocks_count, left_bytes = divmod(len(bs), 3)
    for i in range(blocks_count):
        coding_int = int.from_bytes(bs[3 * i:3 * i + 3], 'little')
        block = VariantBase64Dict[coding_int & 0x3f]
        block += VariantBase64Dict[(coding_int >> 6) & 0x3f]
        block += VariantBase64Dict[(coding_int >> 12) & 0x3f]
        block += VariantBase64Dict[(coding_int >> 18) & 0x3f]
        result += block.encode()
    if left_bytes == 0:
        return result
    elif left_bytes == 1:
        coding_int = int.from_bytes(bs[3 * blocks_count:], 'little')
        block = VariantBase64Dict[coding_int & 0x3f]
        block += VariantBase64Dict[(coding_int >> 6) & 0x3f]
        result += block.encode()
        return result
    else:
        coding_int = int.from_bytes(bs[3 * blocks_count:], 'little')
        block = VariantBase64Dict[coding_int & 0x3f]
        block += VariantBase64Dict[(coding_int >> 6) & 0x3f]
        block += VariantBase64Dict[(coding_int >> 12) & 0x3f]
        result += block.encode()
        return result

def EncryptBytes(key: int, bs: bytes):
    result = bytearray()
    for i in range(len(bs)):
        result.append(bs[i] ^ ((key >> 8) & 0xff))
        key = result[-1] & key | 0x482D
    return bytes(result)

class LicenseType:
    Professional = 1
    Educational = 3
    Persional = 4

def GenerateLicenseInMemory(Type: LicenseType, Count: int, UserName: str, MajorVersion: int, MinorVersion: int):
    assert Count >= 0
    LicenseString = '%d#%s|%d%d#%d#%d3%d6%d#%d#%d#%d#' % (
        Type, UserName, MajorVersion, MinorVersion,
        Count,
        MajorVersion, MinorVersion, MinorVersion,
        0, 0, 0
    )
    EncodedLicenseString = VariantBase64Encode(EncryptBytes(0x787, LicenseString.encode())).decode()
    memory_file = io.BytesIO()
    with zipfile.ZipFile(memory_file, 'w', zipfile.ZIP_DEFLATED) as zf:
        zf.writestr('Pro.key', data=EncodedLicenseString)
    memory_file.seek(0)
    return memory_file

@app.route('/')
def index():
    return send_file('index.html')

# 修改点：添加 methods=['GET', 'POST'] 以支持表单提交
@app.route('/gen', methods=['GET', 'POST'])
def generate_and_download_license():
    # 修改点：根据请求方式选择获取参数的方法
    if request.method == 'POST':
        name = request.form.get('name')
        version = request.form.get('ver')
        count_str = request.form.get('count', '1')
    else:
        name = request.args.get('name')
        version = request.args.get('ver')
        count_str = request.args.get('count', '1')
    
    if not name or not version:
        return make_response("错误：必须提供 'name' 和 'ver' 参数", 400)

    try:
        count = int(count_str)
        MajorVersion, MinorVersion = version.split('.')[0:2]
        MajorVersion = int(MajorVersion)
        MinorVersion = int(MinorVersion)
    except (ValueError, IndexError):
        return make_response("错误：版本号 'ver' 格式不正确，应为 '主版本号.次版本号' (例如: 25.2)", 400)

    license_file_stream = GenerateLicenseInMemory(
        LicenseType.Professional, count, name, MajorVersion, MinorVersion
    )

    return send_file(
        license_file_stream,
        mimetype='application/zip',
        as_attachment=True,
        download_name='Custom.mxtpro'
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
