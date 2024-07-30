# Maintainer: jsusmachaca <falcorgd@gmail.com>

pkgname=qtheme
pkgver=1.3
pkgrel=1
pkgdesc="Tool for management qtile desktop environment"
url='https://github.com/jsusmachaca/qtheme'
arch=('any')
license=('MIT')
depends=('python>=3.12' 'qtile' 'kitty' 'fastfetch')
source=(${pkgname}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('1c9b511c89bd023407542aa8a7e55758fdfd0bf18676ed4b441bee2c0c261dc0390c38b657fd02951641c70ff6c64c8343308543ec72fe1aa0cd593554678756')

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