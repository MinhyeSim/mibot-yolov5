import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Image Classification')
    parser.add_argument('--img_size', default=216, type=int, help='image size')
    parser.add_argument('--batch_size', default=30, type=int, help='batch size')
    parser.add_argument('--num_epochs', default=101, type=int, help='training epoch')
    parser.add_argument('--data', default=2, type=int, help='data')
    parser.add_argument('--cv', default=3, type=int, help='k-folds')
    parser.add_argument('--lr', default=5e-4, type=float, help='learning rate')
    parser.add_argument('--l2', default=0, type=float, help='weight decay')
    parser.add_argument('--ls', default=0.2, type=float, help='label smoothing')
    parser.add_argument('--cutmix', default='n', type=str, help='mixed image')
    parser.add_argument('--type', default='train', type=str, help='train or eval')
    args = parser.parse_args()

    print(args)
    print("Completed")
