import os
import pyflowchart as fc
from pyflowchart import StartNode, EndNode, OperationNode, Flowchart
from IPython.display import Image, display

# Create the flowchart nodes
st = StartNode('Mulai')
io1 = OperationNode('Impor Library: numpy, sympy, scipy, matplotlib')
op1 = OperationNode('Definisikan Simbol: t, m, g, L1, L2, ...')
op2 = OperationNode('Definisikan Fungsi: posisi, kecepatan, energi')
op3 = OperationNode('Hitung Energi Kinetik dan Potensial')
op4 = OperationNode('Hitung Persamaan Lagrange')
op5 = OperationNode('Selesaikan Persamaan Lagrange untuk percepatan sudut')
op6 = OperationNode('Definisikan Fungsi dSdt')
op7 = OperationNode('Selesaikan Persamaan Diferensial: odeint')
op8 = OperationNode('Hitung Koordinat Pendulum')
op9 = OperationNode('Buat Animasi: matplotlib')
e = EndNode('Selesai')

# Connect the nodes
st.connect(io1)
io1.connect(op1)
op1.connect(op2)
op2.connect(op3)
op3.connect(op4)
op4.connect(op5)
op5.connect(op6)
op6.connect(op7)
op7.connect(op8)
op8.connect(op9)
op9.connect(e)

# Create the flowchart
flowchart = Flowchart(st)

# Define the filename for the flowchart PNG output
png_filename = "flowchart.png"

# Save the flowchart as a .flowchart file
flowchart_filename = "flowchart.flowchart"
with open(flowchart_filename, "w") as f:
    f.write(flowchart.flowchart())

# Generate the graphical flowchart using pygraphviz
graph = fc.Flowchart.from_code(flowchart.flowchart()).to_graphviz()
graph.draw(png_filename, prog='dot', format='png')

# Display the flowchart image
display(Image(filename=png_filename))

# Clean up by removing the flowchart and PNG files
os.remove(flowchart_filename)
os.remove(png_filename)
