# Learning a representation. For the time being, this code is learning a convolutional VAE.

import settings
from encoding_conv_vae.conv_vae import get_conv_vae_config, train


def main():
    print("Learn a representation (the vision component)")
    # config = get_conv_vae_config()
    config = get_conv_vae_config('/home/robert/c24git/BerryPick/BerryPicker/src/encoding_conv_vae/config.json')
    train(config)

if __name__ == "__main__":
    main()

