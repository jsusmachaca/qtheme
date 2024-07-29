# Maintainer: jsusmachaca <falcorgd@gmail.com>
pkgname=qtheme
pkgver=1.0
pkgrel=1
pkgdesc="Tool for management qtile desktop environment"
arch=('any')
license=('MIT')
depends=('python')
source=(${pkgname}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)

build() {
	cd $pkgname-$pkgver
	python setup.py build
}
package() {
	cd $pkgname-$pkgver
	python setup.py install --prefix=/usr --root="${pkgdir}" -O1 --skip-build
}