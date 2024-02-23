# Social Network Analysis Tool

This Python tool is designed to perform social network analysis on a dataset of job titles and skills. It constructs a graph representing the relationships between job titles and skills, calculates degree centrality and clustering coefficients for each node, and visualizes the graph for better understanding.

## Features

- **Graph Construction**: Construct a graph where nodes represent job titles and skills, and edges represent the relationship between them.
- **Degree Centrality Calculation**: Calculate the degree centrality for each node in the graph, representing the importance of a node based on the number of connections.
- **Clustering Coefficients Calculation**: Calculate the clustering coefficient for each node, representing the degree to which nodes in a graph tend to cluster together.
- **Graph Visualization**: Visualize the constructed graph using matplotlib for better understanding and analysis.

## Usage

1. **Install Dependencies**: Make sure you have Python installed on your system. Install the required dependencies using pip:
pip install -r requirements.txt

2. **Prepare Dataset**: Prepare your dataset in CSV format. Each row should contain a job title and a list of associated skills separated by commas.

3. **Run the Tool**: Run the `main.py` script and provide the path to your dataset as input:

python main.py --dataset <path_to_dataset.csv>


4. **Interpret Results**: After running the tool, you will see visualizations of the constructed graph along with degree centrality and clustering coefficient values for each node.

## Sample Dataset

You can use the provided `jobs.csv` file as a sample dataset to test the tool. This dataset contains a list of job titles and associated skills.

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request on GitHub.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
