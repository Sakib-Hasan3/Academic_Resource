#include <iostream>
#include <vector>
#include <limits.h>

using namespace std;

int main() 
{
    // Step 1: Initialize the adjacency matrix based on the image
    vector<vector<int>> adjMatrix = {
        {7, 5, 0, 0},
        {7, 0, 3, 2},
        {0, 3, 0, 1},
        {4, 0, 0, 1}
    };
    int numNodes = adjMatrix.size();

    // Display the initial matrix
    cout << "Initial graph:\n";
    for (const auto& row : adjMatrix) {
        for (int weight : row) {
            cout << weight << " ";
        }
        cout << "\n";
    }

    // Step 2: Add an extra node
    numNodes++;
    for (auto &row : adjMatrix) row.push_back(0);  // Add a column of 0s
    adjMatrix.push_back(vector<int>(numNodes, 0)); // Add a row of 0s

    cout << "\nGraph after adding an extra node:\n";
    for (const auto& row : adjMatrix) {
        for (int weight : row) {
            cout << weight << " ";
        }
        cout << "\n";
    }

    // Step 3: Add new edges
    adjMatrix[0][4] = 6; // Connect new node (node 4) to node 0
    adjMatrix[4][0] = 6; // Undirected graph
    adjMatrix[2][4] = 4; // Connect new node (node 4) to node 2
    adjMatrix[4][2] = 4; // Undirected graph

    cout << "\nGraph after adding more edges:\n";
    for (const auto& row : adjMatrix) {
        for (int weight : row) {
            cout << weight << " ";
        }
        cout << "\n";
    }

    // Step 4: Delete the edge with the maximum weight
    int maxWeight = INT_MIN, u = -1, v = -1;
    for (int i = 0; i < numNodes; ++i) {
        for (int j = i + 1; j < numNodes; ++j) {
            if (adjMatrix[i][j] > maxWeight) {
                maxWeight = adjMatrix[i][j];
                u = i;
                v = j;
            }
        }
    }
    if (u != -1 && v != -1) {
        adjMatrix[u][v] = 0;
        adjMatrix[v][u] = 0;
        cout << "\nDeleted edge between " << u << " and " << v << " with weight " << maxWeight << ".\n";
    }

    // Display the final matrix
    cout << "\nGraph after deleting the edge with the maximum weight:\n";
    for (const auto& row : adjMatrix) {
        for (int weight : row) {
            cout << weight << " ";
        }
        cout << "\n";
    }

    return 0;
}
