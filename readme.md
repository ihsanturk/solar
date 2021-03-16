# solar
[![built with nix](https://builtwithnix.org/badge.svg)](https://builtwithnix.org)

Create beautiful generative solar system images using
[gruvbox](https://github.com/morhetz/gruvbox-contrib) as a color palette.  If
you have [`nix` flakes
install](https://nixos.wiki/wiki/Flakes#Installing_flakes)ed, all you have to
do to get a random solar system image is:

```
nix run github:ihsanturk/solar -- solar.png --orbit --gaps
```
And open the `./noised-solar.png`

![example image created with solar](https://i.imgur.com/lBambwF.png)

### notes

* If you don't know what [`nix`](https://nixos.org) is, you are probably
  missing out a great software.
* The idea and big amount of the code forked from
  [erdavids/Generative-Space-System](https://github.com/erdavids/Generative-Space-System)
