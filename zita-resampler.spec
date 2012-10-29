Summary:	Zita resampler library
Name:		zita-resampler
Version:	1.3.0
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	http://kokkinizita.linuxaudio.org/linuxaudio/downloads/%{name}-%{version}.tar.bz2
# Source0-md5:	74c12e2280008f63ac9f2670fe4cf79b
BuildRequires:	fftw3-single-devel
BuildRequires:	libstdc++-devel
Patch0:		%{name}-make.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags	-ffast-math

%description
Zita resampler library.

%package devel
Summary:	Header files for zita-resampler library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This is the package containing the header files for
zita-resampler library.

%prep
%setup -q
%patch0 -p1

%build
%{__make} -C libs \
	CXX="%{__cxx}"		\
	LIBDIR=%{_libdir}	\
	OPTFLAGS="%{rpmcflags}"	\
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C libs install	\
	LIBDIR=%{_libdir}	\
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libzita-resampler.so.?
%attr(755,root,root) %{_libdir}/libzita-resampler.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libzita-resampler.so
%{_includedir}/%{name}

