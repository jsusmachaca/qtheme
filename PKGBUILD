# Maintainer: jsusmachaca <falcorgd@gmail.com>
pkgname=qtheme
pkgver=1.0
pkgrel=1
pkgdesc="Tool for management qtile desktop environment"
url='https://github.com/jsusmachaca/qtheme'
arch=('any')
license=('MIT')
depends=('python>=3.12' 'qtile' 'kitty' 'fastfetch')
source=(${pkgname}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('89e5af37a7267f1ef327f14e9f7d1def2b0b214e83122e0b67ecc67fe532d2e71593ad572725615d853606df82042004182ad341fb72773610e6ccabd266ee15')

build() {
	cd $pkgname-$pkgver
	python setup.py build
}
package() {
	cd $pkgname-$pkgver
	python setup.py install --prefix=/usr --root="${pkgdir}" -O1 --skip-build
	install -Dm 644 LICENSE -t "${pkgdir}"/usr/share/licenses/${pkgname}
}