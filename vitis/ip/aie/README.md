This design is from AMD AIE examples, only the functionality needed to get into HW was left, all simulation parts were removed for clarity. The explanation below is from the original example.

# Object oriented C++ template class kernels with AI Engine API style
The current graph create 4 individual data paths each moving data from PL through an instance of a datamover kernel back to PL.
By using template C++ class kernels, the data type can be changed when instantiating the kernel in the graph.
The AI Engine API enables portable code across AI Engine device families (AIE1 and AIE2-ML) and is easier to use than intrinsics API.

Note that these examples are basic with focus on readable and compact code using helper functions like vector iterators.
For optimization, techniques used in the old function style kernels can still be applied, but may require mixing AIE API with intrinsics.
```
  0. my_scalar_dm.cpp       : Uses AIE scalar processing to move 32-bit data (cint16) each clock cycle. The data is moved
                              from input to output using scalar iterators.
  1. my_vector_dm.cpp       : Uses AIE vector processing to move 256-bit data (8 lanes of cint16) each clock cycle.
                              The vector registers is used for temporary storage declared as a vector iterator.
  2. my_mul_dm.cpp          : Similar as vector data mover, except that the 8 lanes are passed through the DSP MUL
                              by multiplying with 1. This mimics the pipeline delay vector MUL/MAC signal processing.
  3. my_stream_dm.cpp       : Based on direct stream access of the 32-bit AXI Stream. For AIE1 the native stream interface
                              is 32-bit, so for this example a temporary cint16 variable is used to pass input to output.
                              If used with vector register, the 4:1 conversion from 32 to 128-bit is better to use as this
                              aligns with the vector register. For that case we can read 128-bits of data every
                              4th clock cycle, corresponding to 4 cint16 samples. Similar argument for the output, we
                              write 128-bit data every 4th clock cycle and the 1:4 conversion to 32-bit stream.
```

