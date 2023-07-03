def lightCheck(ldr, led):

    light = ldr.read_u16()
    darkness = round((light / 65535) * 100, 1)

    return darkness