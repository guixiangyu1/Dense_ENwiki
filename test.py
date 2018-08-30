from model.data_utils import CoNLLDataset, minibatches
from model.config import Config

def extract_entity(filename):
    with open(filename) as f:
        for line in f:
            word = line.strip().split(' ')[0]
            tag  = line.strip().split(' ')[-1]
            if tag != 'O':
                with open("{}".format(filename.split('.')[0]+'_entity.txt'), "a") as g:
                    g.write(line)



if __name__ == '__main__':
    extract_entity("data/train1.txt")
    extract_entity("data/test1.txt")
    extract_entity("data/valid1.txt")



    # config = Config()
    #
    # train = CoNLLDataset(config.filename_train, config.processing_word,
    #                      config.processing_tag, config.max_iter)
    #
    # batch_size = config.batch_size
    # for i, (words, labels, masks) in enumerate(minibatches(train, batch_size)):
    #     print(masks)
    #     for word in words:
    #         for i in word:
    #             print(i)
    #     # print(labels)
    #     break


    # with open("data/enwiki_match_title.txt") as f:
    #     i = 0
    #     for line in f:
    #         if "None" in line:
    #             i += 1
    #     print(i)


