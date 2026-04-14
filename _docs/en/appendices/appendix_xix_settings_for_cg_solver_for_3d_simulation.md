---
lang: en
title: "Appendix XIX Settings for CG solver for 3D simulation"
---

# Appendix XIX: Settings for CG solver for 3D simulation

AXIX.1. Level of fill in

AXIX.2. Method of partitioning

New Conjugate Gradient (CG) solver setting has two parameters of "Level of fill in" and "Partitioning". Both terminologies are commonly used in describing the iterative methods based on the incomplete LU decomposition method.

## Level of fill in

The profile of matrix based on FEM is originally banded and there are non-zero off-diagonal values between all connected nodes of FEM mesh.

During the factorization of a matrix to solve a set of equations (similar to the elimination process in the Gaussian elimination method), the off-diagonal value, originally zero, is gradually filled.

The level of fill "0" means the original matrix.

The level of fill "1" means that any new filling is allowed between the interaction of non-zero terms in the original matrix, otherwise, it is ignored.

The level of fill "2" means that any new filling is allowed between the interaction of non-zero terms in the "level 1" matrix, otherwise, it is ignored.

And go on.

Thus, the decomposed matrices prepared for the iterative method become more close to the exact as the level of fill-in increases, but the computational time increases greatly. In other words, the number of iterations can be reduced with a higher level of fill, but the cost to get a pre-conditioner becomes expensive. On the other hand, the number of iterations can be increased or may not converge with a lower level of fill although the cost to get a pre-conditioner is cheap.

The optimal value depends on each problem (the type of manufacturing process, the mesh topology, the number of nodes and so on).

Our default value is selected as 4 based on our extensive testing.

The users may try to find a better value for their specific problem.

## Method of partitioning

The partitioning has two meaning in our algorithm: for best node numbering and for evenly distribution of computation for multiple processors. Depending on the node numbering, the amount of filling during factorization explained previously can be increased greatly. We had tested various different methods and selected the default method with some modifications.

For multiple processors, it is better to decompose the whole domain into a number of sub-domains having a minimum interface between sub-domains. We do partitioning first with METIS and then adjust the sub-domains from METIS by changing the interface suitable for our algorithm. Thus, we recommend using our default value for the method of partitioning.
