import collections
import math
import os
import random
import zipfile
import numpy as np
import urllib
import tensorflow as tf
# with tf.Session() as sess:
#     with tf.variable_scope("Test"):
#         x = tf.Variable(initial_value=[[1,2],[4,5]],expected_shape=[2,2],name="x")
#
#     # a = tf.matmul(x, [[0, 0],[0, 0]])
#         y = tf.get_variable("y", initializer=[[1,2],[2,3]])
#         print(y)
#     # init = tf.global_variables_initializer().run()
#         tf.variables_initializer([x, y]).run()
#
#         x_, y_ = sess.run([x, y])
#
#         print(x_, y_)
print(np.exp(1))