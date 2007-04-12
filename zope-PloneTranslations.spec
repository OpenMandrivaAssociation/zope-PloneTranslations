%define product		PloneTranslations
%define ver		2.6.1
%define rel		1

%define zope_minver	2.7

%define zope_home	%{_prefix}/lib/zope
%define software_home	%{zope_home}/lib/python


Summary:	PloneTranslations contains recent i18n files (*.po) for Plone
Name:		zope-%{product}
Version:	%{ver}
Release:	%mkrel %{rel}
License:	GPL
Group:		System/Servers
Source:		http://plone.org/products/plonetranslations/releases/%{version}/PloneTranslations-%{version}.tar.bz2
URL:		http://plone.org/products/plonetranslations
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch:	noarch
Requires:	zope >= %{zope_minver}
Requires:	zope-Archetypes


%description
PloneTranslations contains recent i18n files (*.po) for Plone.
Starting with Plone 2.1, PloneTranslations will ship as own 
Product (but still included in Plone, of course).

%prep
%setup -c -q

rm -rf `find -type d -name .svn`

%build
# Not much, eh? :-)


%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}/%{software_home}/Products
%{__cp} -a * %{buildroot}%{software_home}/Products/


%clean
%{__rm} -rf %{buildroot}

%post
if [ "`%{_prefix}/bin/zopectl status`" != "daemon manager not running" ] ; then
	service zope restart
fi

%postun
if [ -f "%{_prefix}/bin/zopectl" ] && [ "`%{_prefix}/bin/zopectl status`" != "daemon manager not running" ] ; then
	service zope restart
fi

%files
%defattr(-, root, root, 0755)
%{software_home}/Products/*




