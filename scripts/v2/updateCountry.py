from pathlib import Path

def update_country(country_name):
    packages_folder = Path('/home/jerry/react-maps/packages')
    country_dir = packages_folder / country_name
    src_dir_path = country_dir / 'src'
    country_name_capitalized = country_name.capitalize()
    country_file_path = src_dir_path / f'{country_name_capitalized}.tsx'

    country_file_path.write_text(f'''import React, {{ useEffect }} from 'react';
import {{ drawPath, stateCode, constants, viewBox }} from './constants';
import useMousePosition from './hooks/mouseTrack';
import {{ useState }} from 'react';

const {country_name_capitalized} = ({{
  type,
  size,
  mapColor,
  strokeColor,
  strokeWidth,
  hoverColor,
  onSelect,
  hints,
  selectColor,
  hintTextColor,
  hintBackgroundColor,
  hintPadding,
  hintBorderRadius,
}}: {country_name_capitalized}Props) => {{
  if (type === 'select-single') {{
    return (
      <{country_name_capitalized}Single
        type="select-single"
        size={{size}}
        selectColor={{selectColor}}
        mapColor={{mapColor}}
        strokeColor={{strokeColor}}
        strokeWidth={{strokeWidth}}
        hoverColor={{hoverColor}}
        hints={{hints}}
        onSelect={{onSelect}}
        hintTextColor={{hintTextColor}}
        hintBackgroundColor={{hintBackgroundColor}}
        hintPadding={{hintPadding}}
        hintBorderRadius={{hintBorderRadius}}
      />
    );
  }} else if (type === 'select-multiple') {{
    return (
      <{country_name_capitalized}Multiple
        type="select-multiple"
        size={{size}}
        selectColor={{selectColor}}
        mapColor={{mapColor}}
        strokeColor={{strokeColor}}
        strokeWidth={{strokeWidth}}
        onSelect={{onSelect}}
        hoverColor={{hoverColor}}
        hints={{hints}}
        hintTextColor={{hintTextColor}}
        hintBackgroundColor={{hintBackgroundColor}}
        hintPadding={{hintPadding}}
        hintBorderRadius={{hintBorderRadius}}
      />
    );
  }} else {{
    return null;
  }}
}};

const {country_name_capitalized}Single = ({{
  size,
  mapColor,
  strokeColor,
  selectColor,
  strokeWidth,
  hoverColor,
  hints,
  onSelect,
  hintTextColor,
  hintBackgroundColor,
  hintPadding,
  hintBorderRadius,
}}: {country_name_capitalized}Props) => {{
  const {{ x, y }} = useMousePosition();
  const [stateHovered, setStateHovered] = useState<string | null>(null);
  const [selectedState, setSelectedState] = useState<string | null>(null);

  useEffect(() => {{
    if (selectedState) {{
      const path = document.getElementById(selectedState);
      if (path) {{
        path.style.fill = selectColor || constants.SELECTED_COLOR;
      }}
    }}
  }}, [selectedState, selectColor]);

  const mapStyle = {{
    width: size || constants.WIDTH,
    fill: mapColor || constants.MAPCOLOR,
    stroke: strokeColor || constants.STROKE_COLOR,
    strokeWidth: strokeWidth || constants.STROKE_WIDTH,
  }};

  const handleMouseEnter = (hoverStateId: string) => {{
    const path = document.getElementById(hoverStateId);
    setStateHovered(hoverStateId);
    if (path) {{
      if (selectedState === hoverStateId) {{
        path.style.fill = selectColor || constants.SELECTED_COLOR;
      }} else {{
        path.style.fill = hoverColor || constants.HOVERCOLOR;
      }}
    }}
  }};

  const handleMouseLeave = (hoverStateId: string) => {{
    const path = document.getElementById(hoverStateId);
    setStateHovered(null);
    if (path) {{
      if (selectedState === hoverStateId) {{
        path.style.fill = selectColor || constants.SELECTED_COLOR;
      }} else {{
        path.style.fill = mapColor || constants.MAPCOLOR;
      }}
    }}
  }};

  const handleClick = (stateCode: string) => {{
    if (selectedState) {{
      const path = document.getElementById(selectedState);
      if (path) {{
        path.style.fill = mapColor || constants.MAPCOLOR;
      }}
    }}
    setSelectedState(stateCode);
    if (onSelect) {{
      onSelect(stateCode);
    }}
  }};

  return (
    <>
      <div className="map" style={{mapStyle}}>
        <svg version="1.1" id="svg2" x="0px" y="0px" viewBox={{viewBox}}>
          {{stateCode?.map((stateCode: string, index: number) => (
            <path
              key={{index}}
              onClick={{() => handleClick(stateCode)}}
              onMouseEnter={{() => handleMouseEnter(stateCode)}}
              onMouseLeave={{() => handleMouseLeave(stateCode)}}
              id={{stateCode}}
              d={{drawPath[stateCode as keyof typeof drawPath]}}
            />
          ))}}
        </svg>
      </div>
      {{hints && (
        <div style={{{{position:'fixed',top:0}}}}>
          {{stateHovered && (
            <div
              style={{{{
                position: 'absolute',
                top: y + 20,
                left: x + 20,
                backgroundColor: hintBackgroundColor || 'white',
                padding: hintPadding || '10px',
                borderRadius: hintBorderRadius || '5px',
                border: '1px solid #ccc',
                color: hintTextColor || 'black',
              }}}}
            >
              {{stateHovered}}
            </div>
          )}}
        </div>
      )}}
    </>
  );
}};

const {country_name_capitalized}Multiple = ({{
  size,
  selectColor,
  mapColor,
  strokeColor,
  strokeWidth,
  hoverColor,
  hints,
  hintTextColor,
  hintBackgroundColor,
  hintPadding,
  hintBorderRadius,
  onSelect,
}}: {country_name_capitalized}Props) => {{
  const [selectedStates, setSelectedStates] = useState<string[]>([]);
  const {{ x, y }} = useMousePosition();
  const [stateHovered, setStateHovered] = useState<string | null>(null);

  useEffect(() => {{
    selectedStates.forEach((stateCode) => {{
      const path = document.getElementById(stateCode);
      if (path) {{
        path.style.fill = selectColor || constants.SELECTED_COLOR;
      }}
    }});
  }}, [selectedStates, selectColor]);

  const mapStyle = {{
    width: size || constants.WIDTH,
    fill: mapColor || constants.MAPCOLOR,
    stroke: strokeColor || constants.STROKE_COLOR,
    strokeWidth: strokeWidth || constants.STROKE_WIDTH,
  }};

  const handleClick = (stateCode: string) => {{
    if (selectedStates.includes(stateCode)) {{
      const remove_state_code = selectedStates.filter(
        (state) => state !== stateCode
      );
      setSelectedStates(remove_state_code);
      const path = document.getElementById(stateCode);
      if (path) {{
        path.style.fill = mapColor || constants.MAPCOLOR;
      }}
    }} else {{
      setSelectedStates([...selectedStates, stateCode]);
    }}
    if (onSelect) {{
      onSelect(stateCode, selectedStates);
    }}
  }};

  const handleMouseEnter = (hoverStateId: string) => {{
    const path = document.getElementById(hoverStateId);
    if (path) {{
      if (selectedStates.includes(hoverStateId)) {{
        path.style.fill = selectColor || constants.SELECTED_COLOR;
      }} else {{
        path.style.fill = hoverColor || constants.HOVERCOLOR;
      }}
    }}
    setStateHovered(hoverStateId);
  }};

  const handleMouseLeave = (hoverStateId: string) => {{
    const path = document.getElementById(hoverStateId);
    if (path) {{
      if (selectedStates.includes(hoverStateId)) {{
        path.style.fill = selectColor || constants.SELECTED_COLOR;
      }} else {{
        path.style.fill = mapColor || constants.MAPCOLOR;
      }}
    }}
    setStateHovered(null);
  }};

  return (
    <>
      <div className="map" style={{mapStyle}}>
        <svg version="1.1" id="svg2" x="0px" y="0px" viewBox={{viewBox}}>
          {{stateCode?.map((stateCode: string, index: number) => (
            <path
              key={{index}}
              onClick={{() => handleClick(stateCode)}}
              onMouseEnter={{() => handleMouseEnter(stateCode)}}
              onMouseLeave={{() => handleMouseLeave(stateCode)}}
              id={{stateCode}}
              d={{drawPath[stateCode as keyof typeof drawPath]}}
            />
          ))}}
        </svg>
      </div>
      {{hints && (
        <div>
          {{stateHovered && (
            <div
              style={{{{
                position: 'absolute',
                top: y + 20,
                left: x + 20,
                backgroundColor: hintBackgroundColor || 'white',
                padding: hintPadding || '10px',
                borderRadius: hintBorderRadius || '5px',
                border: '1px solid #ccc',
                color: hintTextColor || 'black',
              }}}}
            >
              {{stateHovered}}
            </div>
          )}}
        </div>
      )}}
    </>
  );
}};

export interface {country_name_capitalized}Props {{
  type: 'select-single' | 'select-multiple';
  size?: number;
  mapColor?: string;
  strokeColor?: string;
  strokeWidth?: number;
  hoverColor?: string;
  selectColor?: string;
  hints?: boolean;
  hintTextColor?: string;
  hintBackgroundColor?: string;
  hintPadding?: string;
  hintBorderRadius?: string;
  onSelect?: (state: string, selectedStates?: string[]) => void;
}}

export default {country_name_capitalized};
''')
    
    print(f'Updated {country_name_capitalized} file')


packages_directory = Path("/home/jerry/react-maps/packages")

for package_dir in packages_directory.iterdir():
    if package_dir.is_dir():
        update_country(package_dir.name)
