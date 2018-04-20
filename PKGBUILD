# Script generated with Bloom
pkgdesc="ROS - A copy of the pr2_controller_configuration package, for use in the PR2 simulator. We maintain two copies to allow for controller gains to be set differently between hardware and simulation."
url='http://ros.org/wiki/pr2_controller_configuration_gazebo'

pkgname='ros-kinetic-pr2-controller-configuration-gazebo'
pkgver='2.0.10_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
)

depends=('gazebo'
'ros-kinetic-pr2-controller-manager'
'ros-kinetic-pr2-gripper-action'
'ros-kinetic-pr2-head-action'
'ros-kinetic-single-joint-position-action'
)

conflicts=()
replaces=()

_dir=pr2_controller_configuration_gazebo
source=()
md5sums=()

prepare() {
    cp -R $startdir/pr2_controller_configuration_gazebo $srcdir/pr2_controller_configuration_gazebo
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

