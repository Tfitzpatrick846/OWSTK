function satHandles = loadTelesatConstellation(root)

scenario = root.CurrentScenario;

Re = 6378;
alt = 1000;
inc = 99.5;
numPlanes = 3;
numSatsPerPlane = 12;

for plane = 1:numPlanes
  RAAN = 0 + (plane-1)*63.2;
  TrueAnomalyOffset = 0;
  
  for sats = 1:numSatsPerPlane
    
    % orbit parameters
    apogee = Re+alt;
    perigee = Re+alt;
    trueAnomaly = TrueAnomalyOffset+(sats-1)*360/numSatsPerPlane;
    
    % create satellite
    satName = sprintf('Telesat_pol%02.f%02.f', plane, sats);
    satellite = scenario.Children.New('eSatellite', satName);
    
    % set orbit
    keplerian = satellite.Propagator.InitialState.Representation.ConvertTo('eOrbitStateClassical');
    keplerian.SizeShapeType = 'eSizeShapeAltitude';
    keplerian.LocationType = 'eLocationTrueAnomaly';
    keplerian.SizeShape.PerigeeAltitude = apogee;
    keplerian.SizeShape.ApogeeAltitude = perigee;
    keplerian.Orientation.Inclination = inc;
    keplerian.Orientation.ArgOfPerigee = 0;
    keplerian.Orientation.AscNode.Value = RAAN;
    keplerian.Location.Value = trueAnomaly;
    satellite.Propagator.InitialState.Representation.Assign(keplerian);
    satellite.Propagator.Propagate;
    
    % set graphics
    graphics = satellite.Graphics;
    graphics.SetAttributesType('eAttributesBasic');
    attributes = graphics.Attributes;
    attributes.Line.Width = 1;
    attributes.Line.Style = 'eSolid';
    attributes.Inherit = false;
    attributes.Color = 16776960;
    attributes.MarkerStyle = 'Circle';
    attributes.LabelVisible = false;

  end
  
end
% 
% sub_plane=2;
% 
% for plane = 1:sub_plane
%   RAAN = 94.8 + (plane-1)*63.2;
%   TrueAnomalyOffset = 15;
%   
%   for sats = 1:numSatsPerPlane
%     satName = ['Satellite/Telesat_pol' sprintf('%02.f', plane+numPlanes) sprintf('%02.f', sats)];
%     M = TrueAnomalyOffset+(sats-1)*360/numSatsPerPlane;
%     root.ExecuteCommand(['New / */Satellite Telesat_pol' sprintf('%02.f', plane+numPlanes) sprintf('%02.f', sats)]);
%     root.ExecuteCommand(['SetState */' satName...
%       ' Classical J2Perturbation "18 Sep 2017 16:00:00.000" "18 Feb 2018 16:00:00.000" 60 J2000 "UseAnalysisStartTime" ' num2str(1000*(alt+Re))...
%       ' 0 ' num2str(inc) ' 0 ' num2str(RAAN) ' ' num2str(M)]);
%     root.ExecuteCommand(['Graphics */' satName ' Basic LineWidth 1']);
%     root.ExecuteCommand(['Graphics */' satName ' Basic Inherit Off']);
%     root.ExecuteCommand(['Graphics */' satName ' Basic Orbit On']);
%     root.ExecuteCommand(['Graphics */' satName ' Basic Label Off']);
%     root.ExecuteCommand(['Graphics */' satName ' Basic Color purple']);
%     root.ExecuteCommand(['VO */' satName ' Marker Size 5']);
%     root.ExecuteCommand(['VO */' satName ' Model Show Off']);
%     root.ExecuteCommand(['VO */' satName ' ModelDetail Set ModelLabel 0 MarkerLabel 0']);
%     root.ExecuteCommand(['SetAttitude */' satName ' Profile AlignConstrain PR 0 0 "Nadir(Centric)" Axis 1 0 0 "North"']);
%   end
%   clc
%   disp(plane+numPlanes)
% end
% 
% for plane = 1:1
%   RAAN = 31.6;
%   TrueAnomalyOffset = 15;
%   
%   for sats = 1:numSatsPerPlane
%     satName = ['Satellite/Telesat_pol' sprintf('%02.f', plane+5) sprintf('%02.f', sats)];
%     M = TrueAnomalyOffset+(sats-1)*360/numSatsPerPlane;
%     root.ExecuteCommand(['New / */Satellite Telesat_pol' sprintf('%02.f', plane+5) sprintf('%02.f', sats)]);
%     root.ExecuteCommand(['SetState */' satName...
%       ' Classical J2Perturbation "18 Sep 2017 16:00:00.000" "18 Feb 2018 16:00:00.000" 60 J2000 "UseAnalysisStartTime" ' num2str(1000*(alt+Re))...
%       ' 0 ' num2str(inc) ' 0 ' num2str(RAAN) ' ' num2str(M)]);
%     root.ExecuteCommand(['Graphics */' satName ' Basic LineWidth 1']);
%     root.ExecuteCommand(['Graphics */' satName ' Basic Inherit Off']);
%     root.ExecuteCommand(['Graphics */' satName ' Basic Orbit On']);
%     root.ExecuteCommand(['Graphics */' satName ' Basic Label Off']);
%     root.ExecuteCommand(['Graphics */' satName ' Basic Color purple']);
%     root.ExecuteCommand(['VO */' satName ' Marker Size 5']);
%     root.ExecuteCommand(['VO */' satName ' Model Show Off']);
%     root.ExecuteCommand(['VO */' satName ' ModelDetail Set ModelLabel 0 MarkerLabel 0']);
%     root.ExecuteCommand(['SetAttitude */' satName ' Profile AlignConstrain PR 0 0 "Nadir(Centric)" Axis 1 0 0 "North"']);
%   end
%   clc
%   disp(plane+5)
% end
% 
% alt1 = 1248;
% inc1 = 37.4;
% numPlanes1 = 5;
% numSatsPerPlane1 = 9;
% 
% for plane = 1:numPlanes1
%   RAAN = 0 + (plane-1)*72;
%   TrueAnomalyOffset = 0;
%   
%   for sats = 1:numSatsPerPlane1
%     satName = ['Satellite/Telesat_inc' sprintf('%02.f', plane) sprintf('%02.f', sats)];
%     M = TrueAnomalyOffset+(sats-1)*360/numSatsPerPlane1;
%     root.ExecuteCommand(['New / */Satellite Telesat_inc' sprintf('%02.f', plane) sprintf('%02.f', sats)]);
%     root.ExecuteCommand(['SetState */' satName...
%       ' Classical J2Perturbation "18 Sep 2017 16:00:00.000" "18 Feb 2018 16:00:00.000" 60 J2000 "UseAnalysisStartTime" ' num2str(1000*(alt1+Re))...
%       ' 0 ' num2str(inc1) ' 0 ' num2str(RAAN) ' ' num2str(M)]);
%     root.ExecuteCommand(['Graphics */' satName ' Basic LineWidth 1']);
%     root.ExecuteCommand(['Graphics */' satName ' Basic Inherit Off']);
%     root.ExecuteCommand(['Graphics */' satName ' Basic Orbit On']);
%     root.ExecuteCommand(['Graphics */' satName ' Basic Label Off']);
%     root.ExecuteCommand(['Graphics */' satName ' Basic Color red']);
%     root.ExecuteCommand(['VO */' satName ' Marker Size 5']);
%     root.ExecuteCommand(['VO */' satName ' Model Show Off']);
%     root.ExecuteCommand(['VO */' satName ' ModelDetail Set ModelLabel 0 MarkerLabel 0']);
%     root.ExecuteCommand(['SetAttitude */' satName ' Profile AlignConstrain PR 0 0 "Nadir(Centric)" Axis 1 0 0 "North"']);
%   end
%   clc
%   disp(plane+6)
% end
