cmake_minimum_required(VERSION 3.0.0)

message("CALLING MBEDTLS BOSE CMAKELISTS")

include(${CMAKE_CURRENT_BINARY_DIR}/conanbuildinfo.cmake)
include(build/spitfire_common.cmake)
project(SpitfireMbedtls C ASM)

conan_basic_setup(NO_OUTPUT_DIRS SKIP_RPATH KEEP_RPATHS SKIP_STD SKIP_FPIC)

message("CONAN_SPITFIRECORE_ROOT is ${CONAN_SPITFIRECORE_ROOT}")
message("CONAN_INCLUDE_DIRS_SPITFIRECORE is ${CONAN_INCLUDE_DIRS_SPITFIRECORE}")
message("CONAN_LIB_DIRS_SPITFIRECORE is ${CONAN_LIB_DIRS_SPITFIRECORE}")

message("cmake_policy(SET CMP0077 NEW)")
cmake_policy(SET CMP0077 NEW)

message("CMAKE_MAKE_PROGRAM = ${CMAKE_MAKE_PROGRAM}")
message("CMAKE_C_COMPILER   = ${CMAKE_C_COMPILER}")

set(ENABLE_TESTING Off)
set(ENABLE_PROGRAMS Off)
set(CMAKE_C_FLAGS "-kQCC514x_apps -Wall -WnoConstantSignChange -WnoEvaluationOrder -WCharPointerUnaligned -WnoArgUnused -WnoUnused -WnoConstantTest -WnoAccuracyLoss -WnoExplicitQualifier -WnoUnsignedCompare -WnoArgSizeLarger -minim -Xa -apply-b179745-workaround -mark-code-section-type  -O0 -gc-sections -g")

message("CMAKE_SOURCE_DIR   = ${CMAKE_SOURCE_DIR}")
add_subdirectory(${CMAKE_SOURCE_DIR}/../)
