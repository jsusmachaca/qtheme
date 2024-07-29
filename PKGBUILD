# Maintainer: jsusmachaca <falcorgd@gmail.com>

pkgname=qtheme
pkgver=1.2
pkgrel=1
pkgdesc="Tool for management qtile desktop environment"
url='https://github.com/jsusmachaca/qtheme'
arch=('any')
license=('MIT')
depends=('python>=3.12' 'qtile' 'kitty' 'fastfetch')
source=(${pkgname}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('3380df7df16d400b1d4e87aaebf0e3237870f36116b00d47f97f0e05424b7d71712234c9c86c924b4910fb43759180432f90118a4fd4d983b5ffa1ece50c4a77')

build() {
	cd $pkgname-$pkgver
	python setup.py build
}
package() {
	cd $pkgname-$pkgver
	python setup.py install --prefix=/usr --root="${pkgdir}" -O1 --skip-build
	install -Dm 644 LICENSE -t "${pkgdir}"/usr/share/licenses/${pkgname}
	install -Dm 644 README.md -t "${pkgdir}"/usr/share/doc/${pkgname}
}