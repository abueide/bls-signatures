
file(GLOB HEADERS ${CMAKE_CURRENT_SOURCE_DIR}/*.hpp)
source_group("SrcHeaders" FILES ${HEADERS})

add_library(bls
  ${HEADERS}
  ${CMAKE_CURRENT_SOURCE_DIR}/privatekey.cpp
  ${CMAKE_CURRENT_SOURCE_DIR}/bls.cpp
  ${CMAKE_CURRENT_SOURCE_DIR}/elements.cpp
  ${CMAKE_CURRENT_SOURCE_DIR}/schemes.cpp
)

target_include_directories(bls
  PUBLIC
    ${CMAKE_CURRENT_SOURCE_DIR}
    $<$<BOOL:${GMP_FOUND}>:${GMP_INCLUDES}>
        /home/andrea/projects/relic/build/include
        /home/andrea/projects/relic/build/lib/
)

target_compile_definitions(bls
  PRIVATE
    BLSALLOC_SODIUM=1
)

target_link_libraries(bls
  PUBLIC
    relic_s
    sodium
)

install(DIRECTORY /home/andrea/projects/relic/build/include DESTINATION include/chiabls)
install(DIRECTORY /home/andrea/projects/relic/build/lib DESTINATION include/chiabls)
install(FILES ${HEADERS} DESTINATION include/chiabls)
install(FILES $<TARGET_FILE:bls> DESTINATION lib)

if(BUILD_BLS_TESTS)
  include_directories(${CMAKE_CURRENT_SOURCE_DIR}/../contrib/catch)
  add_executable(runtest test.cpp)
  target_link_libraries(runtest PRIVATE bls)
endif()

if(BUILD_BLS_BENCHMARKS)
  add_executable(runbench test-bench.cpp)
  target_link_libraries(runbench PRIVATE bls)
endif()
