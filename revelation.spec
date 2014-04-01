%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	Password manager for GNOME
Name:		revelation
Version:	0.4.14
Release:	1
License:	GPLv2+
Group:		File tools
Url:		http://oss.codepoet.no/revelation/
Source0:	https://bitbucket.org/erikg/%{name}/downloads/%{name}-%{version}.tar.xz
Source1:	%{name}.png
BuildRequires:	desktop-file-utils
BuildRequires:	intltool
BuildRequires:	pkgconfig(pygtk-2.0)
BuildRequires:	%{_lib}crack2-python
BuildRequires:	pkgconfig(gnome-python-2.0)
BuildRequires:	gnome-python-extras
BuildRequires:	gnome-python-desktop
BuildRequires:	gnome-python-gconf
BuildRequires:	gnome-python-gnomevfs
BuildRequires:	python-dbus
BuildRequires:	cracklib-devel
BuildRequires:	pycrypto >= 1.9
BuildRequires:	imagemagick
Requires:	gnome-python
Requires:	gnome-python-gconf
Requires:	gnome-python-gnomevfs
Requires:	python-dbus
Requires:	python-libxml2
Requires:	pycrypto >= 1.9
Requires:	pygtk2.0 >= 2.3.91

%description
Revelation is a password manager for the GNOME desktop, released under
the GNU GPL license. It organizes accounts in a tree structure, and
stores them as AES-encrypted XML files.

%files -f %{name}.lang
%doc AUTHORS ChangeLog README
%{_sysconfdir}/gconf/schemas/*.schemas
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*
%{py_platsitedir}/%{name}
%dir %{_datadir}/icons/hicolor/
%{_datadir}/icons/hicolor/*
%{_datadir}/mime/packages/%{name}.xml
%{_liconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%configure2_5x \
	--disable-mime-update \
	--disable-desktop-update

%make WARN_CFLAGS=""

%install
GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1 %makeinstall_std UPDATE_MIME_DATABASE=true UPDATE_DESKTOP_DATABASE=true
rm -f %{buildroot}%{_libdir}/python%{py_ver}/site-packages/%{name}/*.pyc

# menu entry
desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="X-MandrivaLinux-System-Other" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

mkdir -p %{buildroot}{%{_liconsdir},%{_iconsdir},%{_miconsdir}}
mkdir -p %{buildroot}%{_datadir}/pixmaps
install -m 644 %{SOURCE1} %{buildroot}%{_liconsdir}/%{name}.png
convert -geometry 32x32 %{SOURCE1} %{buildroot}%{_iconsdir}/%{name}.png
convert -geometry 16x16 %{SOURCE1} %{buildroot}%{_miconsdir}/%{name}.png
cp %{SOURCE1} %{buildroot}%{_datadir}/pixmaps

%find_lang %{name}

