'''

The following script was prepared by Alex Ruzicka for usage at Oak Ridge National Laboratory. This script, when
run on an Opentrons OT-2, automates the preparation of a solution used to incubate membrane-enclosed cell-free
expression systems. The following physical preparation must be done before the script is uploaded to the Opentrons
device and run:

-The p300 pipet attachment must be physically mounted on the left side of the device head
-The p10 pipet attachment must by physically attached on the right side of the device head
-A full box of 300 uL pipet tips must be placed on top of slot 1 on the floor of the OT-2
-A full box of 10uL pipet tips must be placed on top of slot 4 on the floor of the OT-2
-A 24-tube rack must be placed over slot 2 of the floor of the OT-2
-1.5mL microcentrifuge tubes containing reagents must be loaded into the tube rack according to the following specification:


+---+-------------------+-----------------------+------------------+------------------+-------------------+-----------------+
|   |         1         |           2           |        3         |        4         |         5         |        6        |
+---+-------------------+-----------------------+------------------+------------------+-------------------+-----------------+
| A | empty tube        | amino acids           | 100 mM ATP       | 500 mMGTP        | 500 mMCTP         | UTP             |
| B | 250 mM Spermidine | 1M Creatine Phosphate | 100 mM DTT       | 0.5 M folic acid | 3.5M K+ glutamate | 500 mM Mg(OAc)2 |
| C | 1M HEPES          | 1M glucose            | RNAse-free water |                  |                   |                 |
| D |                   |                       |                  |                  |                   |                 |
+---+-------------------+-----------------------+------------------+------------------+-------------------+-----------------+



'''



#imports
from Simpsontrons import labware, instruments

#metadata

#custom fundtions
def transfer(instrument, volume, origin, destination = outerSolution):
    if volume > 20 and volume < 30:
        instrument.pick_up_tip()
        instrument.aspirate(volume/3, origin)
        instrument.dispense(volume/3, destination)
        instrument.blowout()
        instrument.aspirate(volume / 3, origin)
        instrument.dispense(volume / 3, destination)
        instrument.blowout()
        instrument.aspirate(volume / 3, origin)
        instrument.dispense(volume / 3, destination)
        instrument.blowout()
        instrument.drop_tip()
    if volume > 10 and volume <= 20:
        instrument.pick_up_tip()
        instrument.aspirate(volume/2, origin)
        instrument.dispense(volume/2, destination)
        instrument.blowout()
        instrument.aspirate(volume / 2, origin)
        instrument.dispense(volume / 2, destination)
        instrument.blowout()
        instrument.drop_tip()
    else:
        instrument.pick_up_tip()
        instrument.aspirate(volume, origin)
        instrument.dispense(volume, destination)
        instrument.blowout()
        instrument.drop_tip()


#instruments
bigpipette = instruments.P300_Single(mount="left", tip_racks= [bigtipbox])
smallpipet = instruments.P10_Single(mount = 'right', tip_racks= [smalltipbox])

#labware
tuberack = labware.load('opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap', slot = '2')
bigtipbox = labware.load('opentrons_96_tiprack_300ul', slot = '1')
smalltipbox = labware.load('opentrons_96_tiprack_10ul', slot = '4')

#reagents
outerSolution = tuberack.wells('A1')
aminos = tuberack.wells('A2')
ATP = tuberack.wells('A3')
GTP = tuberack.wells('A4')
CTP = tuberack.wells('A5')
UTP = tuberack.wells('A6')
Spermidine = tuberack.wells('B1')
creatine_PO4 = tuberack.wells('B2')
DTT = tuberack.wells('B3')
folicAcid = tuberack.wells('B4')
Kglutamate = tuberack.wells('B5')
MgOAc = tuberack.wells('B6')
HEPES = tuberack.wells('C1')
glucose = tuberack.wells('C2')
water = tuberack.wells('C3')

#commands
bigpipette.pick_up_tip()
bigpipette.aspirate(147, water)
bigpipette.dispense(147, outerSolution)
bigpipette.blowout()
bigpipette.drop_tip()

transfer(smallpipet, 2, aminos, outerSolution)

transfer(smallpipet, 11.3, ATP, outerSolution)

transfer(smallpipet, 1.5, GTP, outerSolution

transfer(smallpipet, 1, CTP, outerSolution)

transfer(smallpipet, , UTP, outerSolution)

transfer(smallpipet, 2, Spermidine, outerSolution)

transfer(smallpipet, 3.75 , aminos, outerSolution)

transfer(smallpipet, 4.5, DTT, outerSolution)

transfer(smallpipet, 1, folicAcid, outerSolution)

transfer(smallpipet, 24 Kglutamate, outerSolution)

transfer(smallpipet, 11.3, MgOAc, outerSolution)

transfer(bigpipette, 30, HEPES, outerSolution)

transfer(bigpipette, 60, glucose, outerSolution)
