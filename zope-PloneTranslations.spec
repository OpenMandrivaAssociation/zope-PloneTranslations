%define Product PloneTranslations
%define product plonetranslations
%define name    zope-%{Product}
%define version 3.0.9
%define release %mkrel 3

%define zope_minver	2.7
%define zope_home	%{_prefix}/lib/zope
%define software_home	%{zope_home}/lib/python

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	PloneTranslations contains recent i18n files (*.po) for Plone
License:	GPL
Group:		System/Servers
URL:		http://plone.org/products/%{product}
Source:		http://plone.org/products/%{product}/releases/%{version}/%{Product}-%{version}.tar.gz
Requires:	zope >= %{zope_minver}
Requires:	zope-Archetypes
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
PloneTranslations contains recent i18n files (*.po) for Plone.
Starting with Plone 2.1, PloneTranslations will ship as own Product
(but still included in Plone, of course).

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
%defattr(-,root,root)
%{software_home}/Products/*
