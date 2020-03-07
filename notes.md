- qrack's example loads a lookup table and then creates a statevector for the output
	- Loads it into the registers.. i think

- It uses some lower level functions that ADD and SUB to the accumulator for the registers
- Does it need half reg for control and half for data?  -- I don't think so..
- question is, how can i load a lookup table in qiskit?

- works by entangling the key and the value in the quantum registers

- all key / value pairs are in superposition between an entangled key register and value register
- iteration formula = floor(pi / 4*arcsin^2(1/sqrt(2^N) ) 
- runs iteration of the amplitude amplification algorithm 12 times = 256 for target value
- each register is 8-qubits in simulation
