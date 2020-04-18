//////////////////////////////////////////////////////////////////////////////////////
//
// (C) Daniel Strano and the Qrack contributors 2017-2019. All rights reserved.
//
// This example demonstrates Grover's search, applied for the purpose of finding a value in a lookup table. (This relies
// on the IndexedLDA/IndexedADC/IndexedSBC methods of Qrack. IndexedADC and IndexedSBC can be shown to be unitary
// operations, while IndexedLDA is unitary up to the requirement that the "value register" is set to zero before
// applying the operation.)
//
// Licensed under the GNU Lesser General Public License V3.
// See LICENSE.md in the project root or https://www.gnu.org/licenses/lgpl-3.0.en.html
// for details.

#include <iomanip> // For setw
#include <iostream> // For cout
#include <string>
#include <unordered_list>

// "qfactory.hpp" pulls in all headers needed to create any type of "Qrack::QInterface."
#include "qfactory.hpp"

using namespace Qrack;


void TagValue(bitCapInt targetPerm, QInterfacePtr qReg, bitLenInt valueStart, bitLenInt valueLength)
{
    // Our "oracle" is true for an input of "100" and false for all other inputs.
    qReg->DEC(targetPerm, valueStart, valueLength);
    qReg->ZeroPhaseFlip(valueStart, valueLength);
    qReg->INC(targetPerm, valueStart, valueLength);
}

int main()
{
    int i;

// Hash / Ngram table
std::unordered_map<int, int> gram3_64ent = {
{21120 ,0x0000e0},
{20481 ,0x476574},
{18562 ,0x000060},
{7685 ,0x000040},
{49415 ,0xb80000},
{12554 ,0x004c01},
{29066 ,0x00b800},
{53773 ,0x686973},
{54925 ,0x72616d},
{41742 ,0xffffff},
{62862 ,0x677261},
{10004 ,0xff0000},
{18581 ,0x000100},
{51350 ,0x200000},
{24345 ,0x400000},
{47641 ,0x4ccd21},
{18077 ,0x00e000},
{45088 ,0x002000},
{51232 ,0xb409cd},
{35621 ,0x000001},
{1578 ,0x020000},
{49712 ,0xcd21b8},
{18737 ,0x00004c},
{40499 ,0x080000},
{5556 ,0x000002},
{40373 ,0x005045},
{41781 ,0x000020},
{7222 ,0x000200},
{34359 ,0x000030},
{7865 ,0x00ffff},
{34362 ,0x000300},
{45500 ,0x70726f},
{25538 ,0x0000c0},
{21188 ,0x000050},
{37190 ,0x504500},
{23751 ,0x657373},
{27337 ,0x008000},
{31051 ,0x33322e},
{15948 ,0x010000},
{57294 ,0x697320},
{32084 ,0x410000},
{2390 ,0x040000},
{44374 ,0x00000e},
{47192 ,0x730000},
{25305 ,0x450000},
{41185 ,0x300000},
{612 ,0x000000},
{9701 ,0xffff00},
{42981 ,0x004000},
{14057 ,0x000400},
{16106 ,0x800000},
{28394 ,0x0000ff},
{34157 ,0x0000b8},
{61039 ,0x09cd21},
{36592 ,0x000080},
{2545 ,0x000010},
{27249 ,0x50726f},
{1395 ,0x001000},
{37108 ,0x030000},
{61818 ,0x546869},
{63354 ,0x207072},
{17533 ,0x726f63},
{3198 ,0x100000},
{22271 ,0x000004}
  };

    // ***Grover's search, to find a value in a lookup table***

    // We search for 100, in the lookup table. All values in lookup table are 1 except a single match.
    // We modify Grover's search, to do this. We use Qrack's IndexedLDA/IndexedADC/IndexedSBC methods, which
    // load/add/substract the key-value pairs of a lookup table of classical memory, into superposition in two quantum
    // registers, an index register and a value register. Measurement of either register should always collapse the
    // state in a random VALID key-value pair from the loaded set. The "oracle" tags the target value part, then we
    // "uncompute" to reach a point where we can flip the phase of the initial state. (See
    // https://en.wikipedia.org/wiki/Amplitude_amplification)

    // At the end, we have the target value with high probability, entangled with the index it was loaded in
    // correspondence with.

    // const bitLenInt indexLength = 8;

    // this will be our hash length in bits
    const bitLenInt indexLength = 6;

    // const bitLenInt valueLength = 8;

    // This will be our ngram length in bits , 3-byte ngram = 24-bits
    const bitLenInt valueLength = 24;
    const bitLenInt carryIndex = indexLength + valueLength;

    // We theoretically know that we're looking for a value part of 100.
    const int TARGET_VALUE = 100;
    const string TARGET_NGRAM = "50726f";

    // We theoretically don't know what the key is, but for the example only, we define it to prepare and check the
    // result state.
    const int TARGET_KEY = 230;

    const string TARGET_HASH = "27249";

    // Both CPU and GPU types share the QInterface API.
#if ENABLE_OPENCL
    QInterfacePtr qReg = CreateQuantumInterface(QINTERFACE_OPENCL, 20, 0);
#else
    QInterfacePtr qReg = CreateQuantumInterface(QINTERFACE_CPU, 20, 0);
#endif

    // This array should actually be allocated aligned for best performance, but this will work. We'll talk about
    // alignment for OpenCL in other examples and tutorials.
    unsigned char* toLoad = new unsigned char[1 << indexLength];
    for (i = 0; i < (1 << indexLength); i++) {
        toLoad[i] = 1;
    }
    toLoad[TARGET_KEY] = TARGET_VALUE;

    // Our input to the subroutine "oracle" is 8 bits.
    qReg->SetPermutation(0);
    qReg->H(valueLength, indexLength);
    //qReg->IndexedLDA(valueLength, indexLength, 0, valueLength, toLoad);

    // load 3gram table 64 entries
    qReg->IndexedLDA(valueLength, indexLength, 0, valueLength, gram3_64ent);

    // Twelve iterations maximizes the probablity for 256 searched elements, for example.
    // For an arbitrary number of qubits, this gives the number of iterations for optimal probability.
    int optIter = M_PI / (4.0 * asin(1.0 / sqrt(1 << indexLength)));

    for (i = 0; i < optIter; i++) {
        // The "oracle" tags one value permutation, which we know. We don't know the key, yet, but the search will
        // return it.
        TagValue(TARGET_NGRAM, qReg, 0, valueLength);

        qReg->X(carryIndex);
        qReg->IndexedSBC(valueLength, indexLength, 0, valueLength, carryIndex, gram3_64ent);
        qReg->X(carryIndex);
        qReg->H(valueLength, indexLength);
        qReg->ZeroPhaseFlip(valueLength, indexLength);
        qReg->H(valueLength, indexLength);
        // qReg->PhaseFlip();
        qReg->IndexedADC(valueLength, indexLength, 0, valueLength, carryIndex, gram3_64ent);
        std::cout << "\t" << std::setw(2) << i
                  << "> chance of match:" << qReg->ProbAll(TARGET_NGRAM | (TARGET_HASH << valueLength)) << std::endl;
    }

    qReg->MReg(0, 8);

    std::cout << "After measurement (of value, key, or both):" << std::endl;
    std::cout << "Chance of match:" << qReg->ProbAll(TARGET_NGRAM | (TARGET_HASH << valueLength)) << std::endl;

    free(toLoad);
}
