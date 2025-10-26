{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  name = "ev3dev";
  GREETING = "Python ev3dev env";
  nativeBuildInputs = with pkgs; [
    (python313.withPackages (ps: with ps; [
      ev3dev2
    ]))
  
    evtest
    usbutils
  ];

  shellHook = ''
    echo $GREETING
  '';
}
