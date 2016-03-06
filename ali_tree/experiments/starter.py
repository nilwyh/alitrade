import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
from numpy import *
def run():
    x = tf.placeholder(tf.float32, [None, 784])
    W = tf.Variable(tf.zeros([784, 10]))
    b = tf.Variable(tf.zeros([10]))
    y = tf.nn.softmax(tf.matmul(x, W) + b)
    y_ = tf.placeholder(tf.float32, [None, 10])
    cross_entropy = -tf.reduce_sum(y_*tf.log(y))
    train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)
    init = tf.initialize_all_variables()
    sess = tf.Session()
    sess.run(init)

    data = input_data.read_data_sets('/usr/local/lib/python2.7/dist-packages/tensorflow/models/image/mnist/data', one_hot=True)
    # data_test = input_data.read_data_sets('/usr/local/lib/python2.7/dist-packages/tensorflow/models/image/mnist/data')
    batch_xs_test = data.test.images
    batch_ys_test = data.test.labels
    for i in range(1000):
        batch_xs, batch_ys = data.train.next_batch(100)

        sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})
        correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))
        accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
        print(sess.run(accuracy, feed_dict={x: batch_xs_test, y_: batch_ys_test}))


if __name__ == "__main__":
    run()