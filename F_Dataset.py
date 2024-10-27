class Dataset:
    def __init__(self, source, target, **kwargs):
        self.source = source
        self.target = target
        self.shuffle = kwargs['shuffle']
        self.shift = kwargs['shift']

    def __repr__(self):
        return (f'source: {self.source}, target: {self.target}, '
                f'shift: {self.shift}')

if __name__ == '__main__':
    source = [1,2,3,4]
    targets = [0,0,1,1]
    k = {'shuffle':False, 'shift':10}

    trainset = Dataset(source, targets, **k)
    print(trainset)