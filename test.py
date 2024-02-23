import unittest
import networkx as nx
import matplotlib.pyplot as plt
import csv
import random
from main import construct_graph, calculate_degree_centrality, calculate_clustering_coefficients


class TestJobSkillsGraph(unittest.TestCase):
    def setUp(self):
        # Read the dataset from CSV file
        self.dataset_path = 'jobs.csv'
        with open(self.dataset_path, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            self.dataset = list(reader)

    def test_graph_construction(self):
        # Construct the graph
        G = construct_graph(self.dataset)

        # Assert that all job titles and skills are nodes in the graph
        for entry in self.dataset:
            self.assertTrue(entry['title'] in G.nodes)
            for skill in entry['description'].split(','):
                self.assertTrue(skill.strip()[:5] in G.nodes)

        # Assert that edges are properly created between job titles and skills
        for entry in self.dataset:
            title = entry['title']
            for skill in entry['description'].split(','):
                skill_label = skill.strip()[:5]
                self.assertTrue(G.has_edge(title, skill_label))

    def test_node_attributes(self):
        # Construct the graph
        G = construct_graph(self.dataset)

        # Assert that each skill node has a 'count' attribute
        for node in G.nodes:
            if len(node) == 5:  # Skill node
                self.assertTrue('count' in G.nodes[node])
            else:  # Job title node
                self.assertFalse('count' in G.nodes[node])

    # Add more test cases for other functionalities...


if __name__ == '__main__':
    unittest.main()
