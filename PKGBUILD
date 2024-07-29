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
sha512sums=('77c84ee0c33ebe1477cdb658bebdc197a2bdc10f1f409a5defc836ebe1bb82504685fc402e1e18dc9c5abe2f6aeb66df42f13854bce18d394c6cb184fe3dd07e')

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