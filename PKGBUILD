# Maintainer: jsusmachaca <falcorgd@gmail.com>

pkgname=qtheme
pkgver=1.4
pkgrel=1
pkgdesc="Tool for management qtile desktop environment"
url='https://github.com/jsusmachaca/qtheme'
arch=('any')
license=('MIT')
depends=('python>=3.12' 'qtile' 'kitty' 'fastfetch')
source=(${pkgname}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('0d18419e50377e5e67ec2605c31c261e6b25a485221110b0e049453f03db12e55848162ab71cb8be8225ba4b1f1ece9417e694f14a1675273a752fb8010be01f')

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