#!/bin/bash

# Define directories
BUILD_DIR="build"
INCLUDE_DIR="include"
SRC_DIR="src"

# Define compiler and flags (feel free to adjust)
COMPILER="gcc"
CFLAGS="-Wall -Wextra"

# Check if build directory exists, create it if not
if [ ! -d "$BUILD_DIR" ]; then
    mkdir -p "$BUILD_DIR"
fi

# Compile all source files in src directory
for FILE in "$SRC_DIR"/*.c; do
    # Extract filename without extension
    BASE_FILE=$(basename "$FILE" .c)

    # Compile the file with object file in build directory
    $COMPILER $CFLAGS -c -I "$INCLUDE_DIR" "$FILE" -o "$BUILD_DIR/$BASE_FILE.o"
done

# Link all object files to create the executable
$COMPILER -o "$BUILD_DIR/xerver" "$BUILD_DIR"/*.o

# Print success message
echo "Compiled successfully. Executable: $BUILD_DIR/xerver"
