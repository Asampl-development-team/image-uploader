cmake_minimum_required(VERSION 3.0.0)

project(image-uploader)

install(FILES image-uploader.py DESTINATION handlers)
install(FILES image-uploader-unpack.py TYPE BIN)
