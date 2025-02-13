-- Node Tables

CREATE TABLE Hex (
  id INT64 NOT NULL,
) PRIMARY KEY (id);

CREATE TABLE Provider (
  id INT64 NOT NULL,
  available INT64 NOT NULL,
  rating INT64 NOT NULL,
) PRIMARY KEY (id);

CREATE TABLE Consumer (
  id INT64 NOT NULL,
  searching INT64 NOT NULL,
) PRIMARY KEY (id);

-- Edge Tables

CREATE TABLE HasProvider (
  id INT64 NOT NULL,
  to_id INT64,
  FOREIGN KEY(to_id) REFERENCES Hex(id)
) PRIMARY KEY (id, to_id),
INTERLEAVE IN PARENT Provider ON DELETE CASCADE;

CREATE TABLE HasConsumer (
  id INT64 NOT NULL,
  to_id INT64,
  FOREIGN KEY(to_id) REFERENCES Hex(id)
) PRIMARY KEY (id, to_id),
INTERLEAVE IN PARENT Consumer ON DELETE CASCADE;

CREATE TABLE HasAdjacent (
  id INT64 NOT NULL,
  to_id INT64,
  radius INT64 NOT NULL,
  FOREIGN KEY(to_id) REFERENCES Hex(id)
) PRIMARY KEY (id, to_id),
INTERLEAVE IN PARENT Hex ON DELETE CASCADE;

CREATE OR REPLACE PROPERTY GRAPH HexMatch

  NODE TABLES (
    Hex,
    Provider,
    Consumer
  )

  EDGE TABLES (
    HasProvider
      SOURCE KEY (id) REFERENCES Provider (id)
      DESTINATION KEY (to_id) REFERENCES Hex (id)
      LABEL HAS_PROVIDER,
    HasConsumer
      SOURCE KEY (id) REFERENCES Consumer (id)
      DESTINATION KEY (to_id) REFERENCES Hex (id)
      LABEL HAS_CONSUMER,
    HasAdjacent
      SOURCE KEY (id) REFERENCES Hex (id)
      DESTINATION KEY (to_id) REFERENCES Hex (id)
      LABEL HAS_ADJACENT
  );
