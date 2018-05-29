print("Hello world!")
import tensorflow as tf
#new line
hello = tf.constant('Hello, TensorFlow!')  
 
#Start tf session 
sess = tf.Session() 
 

print(sess.run(hello)) 


