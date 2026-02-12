{ pkgs ? import <nixpkgs> {} }:

let
  pythonEnv = pkgs.python312.withPackages (ps: [
    ps.pyside6
    ps.pyocd
    ps.click
  ]);
in

pkgs.stdenv.mkDerivation {
  pname = "dap-programmer";
  version = "0.1.0";

  src = ./.;

  installPhase = ''
    mkdir -p $out/bin
    mkdir -p $out/lib/dap-programmer

    cp -r backend gui cli tools run_gui.py $out/lib/dap-programmer/

    cat > $out/bin/dap-programmer <<EOF
    #!${pkgs.bash}/bin/bash
    export PYTHONPATH=$out/lib/dap-programmer
    exec ${pythonEnv}/bin/python $out/lib/dap-programmer/run_gui.py
    EOF

    chmod +x $out/bin/dap-programmer
  '';
}

