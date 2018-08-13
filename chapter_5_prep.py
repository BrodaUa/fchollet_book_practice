import os, shutil

original_dataset_dir = '/home/broda/kaggle/dogs-vs-cats/train'
base_dir = '/home/broda/dogs-vs-cats'
os.mkdir(base_dir)

train_dir = os.path.join(base_dir, 'train')
os.mkdir(train_dir)
validation_dir = os.path.join(base_dir, 'validation')
os.mkdir(validation_dir)
test_dir = os.path.join(base_dir, 'test')
os.mkdir(test_dir)

for animal in ['cat','dog']:
    
    train_animal_dir = os.path.join(train_dir, animal)
    os.mkdir(train_animal_dir)

    fnames = ['{}.{}.jpg'.format(animal,i) for i in range(1000)]
    for fname in fnames:
        src = os.path.join(original_dataset_dir, fname)
        dst = os.path.join(train_animal_dir, fname)
        shutil.copyfile(src, dst)

    validation_animal_dir = os.path.join(validation_dir, animal)
    os.mkdir(validation_animal_dir)

    fnames = ['{}.{}.jpg'.format(animal,i) for i in range(1000, 1500)]
    for fname in fnames:
        src = os.path.join(original_dataset_dir, fname)
        dst = os.path.join(validation_animal_dir, fname)
        shutil.copyfile(src, dst)

    test_animal_dir = os.path.join(test_dir, animal)
    os.mkdir(test_animal_dir)

    fnames = ['{}.{}.jpg'.format(animal,i) for i in range(1500, 2000)]
    for fname in fnames:
        src = os.path.join(original_dataset_dir, fname)
        dst = os.path.join(test_animal_dir, fname)
        shutil.copyfile(src, dst)


