'use strict';
var app = angular.module("seaporte", ['ngRoute']);

app.config(['$routeProvider', '$locationProvider', function($routeProvider, $locationProvider) {
  $routeProvider.when('/', {
    templateUrl: 'partials/capabilities.html',
  });
  $routeProvider.when('/points-of-contact', {
    templateUrl: 'partials/points-of-contact.html',
  });
  $routeProvider.when('/task-orders', {
    templateUrl: 'partials/task-orders.html',
  });
  $routeProvider.when('/team-information', {
    templateUrl: 'partials/team-information.html',
  });
  $routeProvider.when('/quality-assurance', {
    templateUrl: 'partials/quality-assurance.html',
  });
  $routeProvider.otherwise('/');
  $locationProvider.html5Mode(false)
}]);
