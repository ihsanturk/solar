{

	description = "Solar generative art";

	inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
	inputs.flake-utils.url = "github:numtide/flake-utils";

	outputs = { self, nixpkgs, flake-utils, }:
	flake-utils.lib.eachDefaultSystem (system: let
		pkgs = nixpkgs.legacyPackages.${system};
	in rec {

		solar = {lib, buildPythonApplication, docopt, cairo, pillow}:
			buildPythonApplication rec {
				pname = "solar";
				version = "1.0";
				src = lib.cleanSource ./.;
				doCheck = false;
				propagatedBuildInputs = [
					docopt
					cairo
					pillow
				];
			};

		defaultPackage = pkgs.python3Packages.callPackage solar {};

		defaultApp = {
			type = "app";
			program = "${self.defaultPackage.${system}}/bin/solar";
		};

	});

}

