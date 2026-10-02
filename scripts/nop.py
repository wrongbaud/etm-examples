import sys
from capstone import *

nop_bytes = [0x00,0xBF]

nops = [
    0x8006c60,
    0x8005D0A,
    0x08005ce2,
    0x08005cec,
    0x08005cf6,
    0x08005d00,
    ]


def disassemble(offset,firmware):
    md = Cs(CS_ARCH_ARM,CS_MODE_THUMB+CS_MODE_LITTLE_ENDIAN)
    len = 0
    for target_inst in md.disasm(firmware[offset:],0x8000000+offset):
        print("Target instruction for patch: 0x%x:\t%s\t%s Length: 0x%x" %(target_inst.address, target_inst.mnemonic, target_inst.op_str, target_inst.size))
        len = target_inst.size
        break
    return len

def patch(patch_data,offset,patch_len):
    global nop_bytes
    for x in range(0,patch_len):
        patch_data[offset+x] = nop_bytes[x%2]
        print("Patching with 0x%x" % nop_bytes[x%2])
    return patch_data

def main(infile,outfile):
    program_data = open(infile,'rb').read()
    patch_data = bytearray(program_data)
    for nop_offset in nops:
        nop_offset = nop_offset - 0x8000000
        patch_len = disassemble(nop_offset,program_data)
        patch_data = patch(patch_data,nop_offset,patch_len)
    with open(outfile,'wb') as ofile:
        ofile.write(bytes(patch_data))

if __name__ == "__main__":
    infile = sys.argv[1]
    outfile = sys.argv[2]
    main(infile,outfile)
