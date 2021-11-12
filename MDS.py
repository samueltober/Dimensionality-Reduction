import numpy as np


class MDS:
    def __init__(self, data_filename: str = 'dist_matrix.pkl'):
        self.data_filename = data_filename
        self.dist_matrix = self._load_data()

    def _load_data(self) -> np.ndarray:
        try:
            data = np.load(self.data_filename, allow_pickle=True)
        except FileNotFoundError:
            print("File not found")
            return

        return data

    def _compute_similarity_matrix_from_dist_matrix(self) -> np.ndarray:
        """
        Compute the similarity matrix from the distance matrix using double centering trick
        """
        # centering matrix
        n = self.dist_matrix.shape[0]
        J_c = 1. / n * (np.eye(n) - 1 + (n - 1) * np.eye(n))
        double_centered_matrix = -0.5 * (J_c.dot(self.dist_matrix)).dot(J_c)

        return double_centered_matrix

    def perform_mds(self) -> np.ndarray:
        """
        Multidimensional scaling
        """
        # compute the similarity matrix
        sim_matrix = self._compute_similarity_matrix_from_dist_matrix()

        # compute the eigenvalues and eigenvectors
        eig_vals, eig_vecs = np.linalg.eig(sim_matrix)

        # sort the eigenvalues and eigenvectors
        idx = eig_vals.argsort()[::-1]
        eig_vals = eig_vals[idx]
        eig_vecs = eig_vecs[:, idx]

        # compute the coordinates
        coords = eig_vecs[:, 0:2]

        return coords


if __name__ == '__main__':
    mds_obj = MDS()
    coords = mds_obj.perform_mds()
    print(coords)



