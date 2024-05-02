# To learn more about how to use Nix to configure your environment
# see: https://developers.google.com/idx/guides/customize-idx-env
{ pkgs, ... }: {
  # Which nixpkgs channel to use.
  channel = "stable-23.11"; # or "unstable"

  # Use https://search.nixos.org/packages to find packages
  packages = [
    # pkgs.go
    pkgs.python311
    pkgs.python311Packages.pip
    pkgs.python311Packages.django
    pkgs.python311Packages.asgiref
    pkgs.python311Packages.gunicorn
    pkgs.python311Packages.packaging
    pkgs.python311Packages.sqlparse
    pkgs.python311Packages.tzdata
    pkgs.python311Packages.whitenoise
    # pkgs.nodePackages.nodemon
  ];

  # Sets environment variables in the workspace
  env = {};
  idx = {
    # Search for the extensions you want on https://open-vsx.org/ and use "publisher.id"
    extensions = [
      # "vscodevim.vim"
      "batisteo.vscode-django"
      "bradlc.vscode-tailwindcss"
      "cweijan.dbclient-jdbc"
      "cweijan.vscode-mysql-client2"
      "dsznajder.es7-react-js-snippets"
      "eamodio.gitlens"
      "ecmel.vscode-html-css"
      "esbenp.prettier-vscode"
      "mhutchie.git-graph"
      "mongodb.mongodb-vscode"
      "ms-azuretools.vscode-docker"
      "ms-python.debugpy"
      "ms-python.python"
      "redhat.vscode-xml"
    ];

    # Enable previews
    previews = {
      enable = true;
      previews = {
        # web = {
        #   # Example: run "npm run dev" with PORT set to IDX's defined port for previews,
        #   # and show it in IDX's web preview panel
        #   command = ["npm" "run" "dev"];
        #   manager = "web";
        #   env = {
        #     # Environment variables to set for your server
        #     PORT = "$PORT";
        #   };
        # };
      };
    };

    # Workspace lifecycle hooks
    workspace = {
      # Runs when a workspace is first created
      onCreate = {
        # Example: install JS dependencies from NPM
        # npm-install = 'npm install';
      };
      onStart = {
        # Example: start a background task to watch and re-build backend code
        # watch-backend = "npm run watch-backend";
      };
    };
  };
}
