[app]

# Titulo e dados do app
title = Vivarium Flora Fauna
package.name = vivariumflorafauna
package.domain = org.test

# Codigo fonte
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# Versao do app
version = 0.1

# Requisitos do Python
requirements = python3,kivy

# Configuracoes de tela
orientation = portrait
fullscreen = 0

# Configuracoes do Android
android.api = 33
android.minapi = 24
android.ndk = 25b
android.archs = arm64-v8a
p4a.bootstrap = sdl2

# Desativa alertas de root do terminal
warn_on_root = 0

log_level = 2

[buildozer]
build_dir = ./.buildozer
bin_dir = ./bin
