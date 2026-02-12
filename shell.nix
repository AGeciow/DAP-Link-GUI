{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  packages = [
    (pkgs.python3.withPackages(pypkgs: with pypkgs; [
      pip
      pyocd
      pyside6
      click
      pkgs.qtcreator
    ]))
  ];
}
