import tensorflow as tf

# Create a sample Keras model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(10, activation='relu', input_shape=(784,)),
    tf.keras.layers.Dense(10, activation='softmax')
])

# Save the model in SavedModel format (which includes saved_model.pb)
model.save('my_saved_model', save_format='tf') 
# Alternatively, you can just provide a directory name:
# model.save('my_saved_model_dir') 
