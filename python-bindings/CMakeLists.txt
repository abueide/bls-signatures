
FetchContent_Declare(
  pybind11
  SOURCE_DIR @pybind11_src@
)
FetchContent_MakeAvailable(pybind11)

pybind11_add_module(blspy ${CMAKE_CURRENT_SOURCE_DIR}/pythonbindings.cpp)
target_link_libraries(blspy PRIVATE relic bls)
