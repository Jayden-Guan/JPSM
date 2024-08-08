# JPSM
JPSM:A Privilege Score Model For Libraries.

The security of software applications is increasingly being
threatened by the use of third-party libraries, particularly
from the Node Package Manager (NPM), which can introduce
vulnerabilities. This paper introduces a method for calculat-
ing a privilege score for NPM libraries using static analysis
and the Mir tool. By assigning weighted values to differ-
ent permissions, we provide a quantifiable risk assessment.
Our approach includes a recursive algorithm to evaluate cu-
mulative permissions, enhancing the accuracy of security
evaluations. The paper discusses the implementation of this
method in JavaScript, Python and Node.js, demonstrating its
effectiveness in improving security awareness and encourag-
ing secure coding practices. This model (JPSM) can roughly
estimate the security degree of library
