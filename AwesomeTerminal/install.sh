# Install the Z Shell and set it as default
brew install zsh
chsh -s /bin/zsh

# Install OhMyZsh from https://github.com/ohmyzsh/ohmyzsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

# Instal PowerLevel9k from https://github.com/Powerlevel9k/powerlevel9k
brew tap sambadevi/powerlevel9k
brew install powerlevel9k
echo "source /usr/local/opt/powerlevel9k@0.6.3/powerlevel9k.zsh-theme" >> ~/.zshrc
git clone https://github.com/bhilburn/powerlevel9k.git ~/.oh-my-zsh/custom/themes/powerlevel9k

# Install HackNerd Fonts from https://github.com/ryanoasis/nerd-fonts
brew tap homebrew/cask-fonts
brew cask install font-hack-nerd-font

# Replace default robbyrussell theme with nerdfonts+powerlevel9k
sed -ie "s/ZSH_THEME=\"robbyrussell\"/POWERLEVEL9K_MODE=\"nerdfont-complete\" ZSH_THEME=\"powerlevel9k\/powerlevel9k\"/" ~/.zshrc

# Install colorls, lolcat and artii with all their dependencies (Which is basically installing ruby)
brew install ruby
gem install colorls
gem install artii
gem install lolcat

# Customize PowerLevel9k (I chose these ones because I think they look cool but you can change them)
echo """

# Customize iTerm UI
POWERLEVEL9K_DATE_BACKGROUND="blue"
POWERLEVEL9K_TIME_BACKGROUND="cyan"
POWERLEVEL9K_RAM_BACKGROUND="green"
POWERLEVEL9K_VIRTUALENV_BACKGROUND="yellow1"
POWERLEVEL9K_LEFT_PROMPT_ELEMENTS=(os_icon virtualenv ssh dir vcs newline command_execution_time status)
POWERLEVEL9K_RIGHT_PROMPT_ELEMENTS=(date time ram)
POWERLEVEL9K_PROMPT_ADD_NEWLINE=true

# Aliases to force shell scripts to run from zsh
alias /bin/sh="/usr/local/bin/zsh"
alias /usr/bin/sh="/usr/local/bin/zsh"

# Enable colorls
source $(dirname $(gem which colorls))/tab_complete.sh
alias ls="colorls"

clear
artii "Ad Roll - Next Roll - Roll Works" | lolcat

""" >> ~/.zshrc

