import networkx as nx
from pyvis.network import Network

class GraphVisualizer:
    def __init__(self, js_files, endpoints):
        self.js_files = js_files
        self.endpoints = endpoints

    def visualize(self):
        G = nx.Graph()
        for js in self.js_files:
            G.add_node(js, color='blue')
        for ep in self.endpoints:
            G.add_node(ep, color='red')
            for js in self.js_files:
                G.add_edge(js, ep)

        net = Network(notebook=False, height="750px", width="100%")
        net.from_nx(G)
        net.write_html("graph.html", open_browser=False)  # safe method
        print("[+] Graph saved as graph.html")

