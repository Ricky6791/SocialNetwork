import networkx as nx
import matplotlib.pyplot as plt
import csv
import random

# Read the dataset from CSV file
dataset_path = 'jobs.csv'
with open(dataset_path, 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    dataset = list(reader)

# Randomly sample a subset because too much data makes graph hard to read
random_sample = random.sample(dataset, min(10, len(dataset)))

G = nx.Graph()

# Add nodes (job titles and skills) to the graph
for entry in random_sample:
    title = entry['title'][:10]  # Show the first 10 characters for title nodes to help with clutter
    skills = entry['description'].split(',')  # Split skills based on a delimiter from description

    G.add_node(title)

    for skill in skills:
        skill_label = skill.strip()[:5]  # Show the first 5 characters for skill nodes to help with clutter
        if G.has_node(skill_label):
            # If the skill node already exists, increase a 'count' attribute
            G.nodes[skill_label]['count'] += 1
        else:
            # If the skill node is new, add it with a 'count' attribute set to 1
            G.add_node(skill_label, count=1)
        G.add_edge(title, skill_label)

# Calculate degree centrality
degree_centrality = nx.degree_centrality(G)

# Calculate clustering coefficients
clustering_coefficients = nx.clustering(G)

layout = nx.spring_layout(G)

# Modify node size based on the degree centrality
node_sizes = [degree_centrality[node] * 1000 if node in degree_centrality else 100 for node in G.nodes()]

# Plot the graph with node size representing degree centrality
plt.figure(figsize=(12, 8))
nx.draw(G, layout, with_labels=True, node_size=node_sizes, node_color='lightblue', font_size=10, font_color='black', alpha=0.8)
plt.title("Random Subset of Job Titles and Skills")

# Print degree centrality and clustering coefficients for each node
for node in G.nodes():
    print(f"{node}: Degree Centrality = {degree_centrality.get(node, 0):.3f}, Clustering Coefficient = {clustering_coefficients.get(node, 0):.3f}")

plt.axis('off')
plt.show()

